import api
import regions
import world_cloud

def main():
    generate_cloud("auvergne-rhone-alpes")
    generate_cloud("bourgogne-franche-comte")
    generate_cloud("bretagne")
    generate_cloud("centre-val-de-loire")
    generate_cloud("corse")
    generate_cloud("grand-est")
    generate_cloud("hauts-de-france")
    generate_cloud("ile-de-france")
    generate_cloud("normandie")
    generate_cloud("nouvelle-aquitaine")
    generate_cloud("occitanie")
    generate_cloud("provence-alpes-cote-dazur")
    generate_cloud("pays-de-la-loire")
    generate_cloud("outre-mer")



    #api.idf()

    
def generate_cloud(region): 
    world_cloud.world_cloud(
        api.getToday(region)[1],
        regions.getMask("vierge"),
        region + ".png"
    )


if __name__ == "__main__":
    main()
