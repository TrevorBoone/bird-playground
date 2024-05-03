import sys
from model import create_model, train, plot_history

def main():
    model = create_model(525, (224, 224))
    history = train(model, sys.argv[1], epochs=5)
    plot_history(history)
    model.save("python/ml/models/current.keras")

if __name__=="__main__":
    main()