from setuptools import setup

setup(name='fantasy_football_auction_ai',
      version='0.0.1',
      install_requires=['gym>=0.7.4,<0.9.6', 'fantasy_football_auction>=0.9.96', 'gym_fantasy_football_auction>=1.07',
                        'keras-rl>=0.4.0', 'numpy>=1.13.1', 'h5py>=2.7.1', "matplotlib>=2.1.1", "drawnow>=0.71.3",
                        "tensorforce>=0.3.5.1"],
      packages=['fantasy_football_auction_ai'],
      package_dir={'fantasy_football_auction_ai': 'fantasy_football_auction_ai'},
      package_data={'fantasy_football_auction_ai': ['data/*.csv']},
      extras_require={
        "tf": ["tensorflow>=1.4.1"],
        "tf_gpu": ["tensorflow-gpu>=1.4.1"],
      }
)
