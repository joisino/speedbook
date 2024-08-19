import torch
import torchvision
import torchvision.transforms as transforms
from models import resnet50


class Eval:
    def __init__(self, batch_size=256):
        transform_test = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))]
        )

        testset = torchvision.datasets.CIFAR10(root="./data", train=False, download=True, transform=transform_test)
        self.testsize = len(testset)
        self.testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False)

    def eval(self, model, device):
        model.eval()
        correct = 0
        for inputs, labels in self.testloader:
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()

        return correct / self.testsize


if __name__ == "__main__":
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = resnet50(pretrained=True, download=True)
    model.to(device)

    evaluator = Eval()
    accuracy = evaluator.eval(model, device)
    print(f"Accuracy: {accuracy}")
