import world_cloud
import api

def main():
    world_cloud.world_cloud(api.getToday("ile-de-france")[1])
    world_cloud.world_cloud(api.getToday("auvergne-rhone-alpes")[1])

if __name__ == "__main__":
    main()
