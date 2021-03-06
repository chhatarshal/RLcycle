import hydra
from omegaconf import DictConfig

from rlcycle.build import build_agent


@hydra.main(config_path="../configs/atari/c51.yaml", strict=False)
def main(cfg: DictConfig):
    agent = build_agent(**cfg)
    agent.train()


if __name__ == "__main__":
    main()
