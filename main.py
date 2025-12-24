# frznheiress//codeheiress
# codeheiress@bsky.social
# https://github.com/CodeHeiress/Handtrap-Randomizer.git
import random

hand_trap_list = ["Nibiru, the Primal Being",'Ash Blossom and Joyous Spring','Ghost Belle and Haunted Mansion', 'Droll & Lock Bird', 'Ghost Ogre & Snow Rabbit', 'Infinite Impermanence', 'Dominus Impulse', 'Dominus Purge', 'Dominus Spiral', 'Songs of the Dominators', 'Effect Veiler', 'Mulcharmy Fuwalos', 'Mulcharmy Purulia', 'Mulcharmy Meowls', 'D.D. Crow', 'Bystial Magnamhut', 'Bystial Druiswurm', 'Bystial Baldrake', 'Bystial Saronir', 'Dimension Shifter', 'Retalliating \"C\"', 'Ally of Justice Cycle Reader', 'Herald of Orange Light', 'K9 Izuna']





def randomizer():
    ht = random.choice(hand_trap_list)
    return ht

def main():
    reps = 'y'
    while reps == 'y' or reps == 'Y':
        ht1 = randomizer()
        ht2 = randomizer()
        print(f' Your opponent drew {ht1} and {ht2}')
        reps = input('Continue? [y/n]')


if __name__ == '__main__':
    main()