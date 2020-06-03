import api
import regions
import world_cloud

def main():
    region="ile-de-france"

    world_cloud.world_cloud(
        api.getToday(region)[1],
        regions.getMask(region)
    )

    #api.idf()

if __name__ == "__main__":
    main()
