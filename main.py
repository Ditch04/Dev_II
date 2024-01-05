import argparse
import json
import sys

from tabulate import tabulate


def fileopen(file_path):
    try:
        with open(file_path, 'r') as file:
            ballers = json.load(file)
        return ballers
    except FileNotFoundError:
        raise FileNotFoundError('File not found')


def find_best_scorer(ballers):
    ballers_sorted = sorted(ballers, key=lambda x: float(x['ppg']), reverse=True)
    best_scorer = ballers_sorted[0] if ballers_sorted else None
    best_scorer['name'] += ' *'
    return best_scorer


def find_best_shooter(ballers):
    ballers_sorted = sorted(ballers, key=lambda x: float(x['fg%']), reverse=True)
    best_shooter = ballers_sorted[0] if ballers_sorted else None
    best_shooter['name'] += ' $'
    return best_shooter


def display_on_post(ballers, post):
    if post:
        ballers_filtered = [i for i in ballers if i["position"] == post]
        return ballers_filtered
    return ballers


def min_points(ballers, min):
    if min is not None:
        ballers = [baller for baller in ballers if baller.get('total_points', 0) >= min]
    return ballers


def order_by(ballers, key):
    if key:
        for baller in ballers:
            value = baller.get(key)
            if isinstance(value, (int, float)):
                ballers = sorted(ballers, key=lambda x: x.get(key, 0), reverse=True)
            else:
                ballers = sorted(ballers, key=lambda x: x.get(key, 0))
    return ballers


def select_info(ballers, selection):
    if selection:
        ballers = [{info: baller.get(info, 'N/A') for info in selection} for baller in ballers]
    return ballers


def create_tab(ballers):
    if ballers:
        headers = ballers[0].keys()
        tab = [list(baller.values()) for baller in ballers]
        table = (tabulate(tab, headers, tablefmt='grid'))
        print(table)


def write_in_file(ballers, output_file):
    with open(output_file, 'w') as out_file:
        for baller in ballers:
            out_file.write(str(baller) + '\n')


def parse_args(args):
    parser = argparse.ArgumentParser(description='Baller')
    parser.add_argument('-i', '--input', type=str, required=True, help='Chemin vers le fichier json de joueurs')
    parser.add_argument('-o', '--output', type=str, required=True, help='Chemin vers le fichier texte de sortie')
    parser.add_argument('--order', type=str, help='Trier selon la catégorie demandée')
    parser.add_argument('--position', type=str, help='N\'affiche que les joueurs jouant à ce poste')
    parser.add_argument('--select', type=str, nargs='+', help='Informations sur le joueur à afficher')
    parser.add_argument('--min_points', type=int,
                        help='Ne garde que les joueurs ayant marqué au moins ce nombre de points')

    return parser.parse_args(args)


def main():

    args = parse_args(sys.argv[1:])

    ballers = fileopen(args.input)

    find_best_shooter(ballers)

    find_best_scorer(ballers)

    ballers = order_by(ballers, args.order)

    ballers = display_on_post(ballers, args.position)

    ballers = min_points(ballers, args.min_points)

    ballers = select_info(ballers, args.select)

    create_tab(ballers)

    write_in_file(ballers, args.output)


if __name__ == '__main__':
    main()
