from read_file_module import read_out_csv
from ploter import make_plot
import click


@click.command()
@click.option('--csv_path', default="./data.csv", help='Path to csv')
@click.option('--fig_path', default="./fig.png", help='Path to save fig')
def app(csv_path, fig_path):
    data = read_out_csv(csv_path)
    make_plot(data, fig_path)


if __name__ == '__main__':
    app()