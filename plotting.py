import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    @staticmethod
    def plot_kde(results1, label1, results2, label2, test_name, filename):
        plt.figure(figsize=(8, 5))
        sns.kdeplot(results1, label=label1, fill=True)
        sns.kdeplot(results2, label=label2, fill=True)
        plt.title(f'KDE Plot - {test_name}')
        plt.xlabel('Test Result')
        plt.ylabel('Density')
        plt.legend()
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    @staticmethod
    def plot_cumulative(results1, label1, results2, label2, test_name, filename):
        plt.figure(figsize=(8, 5))
        sns.ecdfplot(results1, label=label1)
        sns.ecdfplot(results2, label=label2)
        plt.title(f'Cumulative Probability Plot - {test_name}')
        plt.xlabel('Test Result')
        plt.ylabel('Cumulative Probability')
        plt.legend()
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
