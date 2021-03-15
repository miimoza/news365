import api
import regions
import world_cloud

def main():
    generate_cloud("ile-de-france")
    generate_cloud("auvergne-rhone-alpes")


    #api.idf()

    
def generate_cloud(region): 
    world_cloud.world_cloud(
        api.getToday(region)[1],
        regions.getMask(region),
        region + ".png"
    )


if __name__ == "__main__":
    main()
