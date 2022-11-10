//ღ(¯`◕‿◕´¯) ♫ ♪ ♫ YuSuF ♫ ♪ ♫ (¯`◕‿◕´¯)ღ

import java.io.IOException;
import java.util.*;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

public class main {

    public static void main(String[] args) throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        Scanner in = new Scanner(System.in);
        game newGame = new game();
        newGame.welcomeSir();
        ships firstShip = new ships("USS-Hawk-19", 6, 1);
        ships secondShip = new ships("USS-Summit-7", 4, 2);
        ships thirdShip = new ships("USS-LengoVlad-11", 2, 3);
        newGame.computerDeployingShips(firstShip.shipLength, firstShip.shipNo);
        newGame.computerDeployingShips(secondShip.shipLength, secondShip.shipNo);
        newGame.computerDeployingShips(thirdShip.shipLength, thirdShip.shipNo);
        System.out.println(newGame.firstShip);
        System.out.println(newGame.secondShip);
        System.out.println(newGame.thirdShip);
        int guessesCounter = 0;
        while (true) {
            int x = in.nextInt();
            int y = in.nextInt();
            newGame.playRogerThatSound();
            String givenCoords = x + "" + y;
            if (newGame.firstShip.contains(givenCoords)) {
                newGame.emptyThatPlace(newGame.firstShip, x, y);
                newGame.showTheHitPlace(x, y);
                newGame.printOceanMap();
                System.out.println("You Hit " + firstShip.shipName + " Sir !");
                System.out.println("Remaining Missiles : " + (15 - guessesCounter));
            } else if (newGame.secondShip.contains(givenCoords)) {
                newGame.emptyThatPlace(newGame.secondShip, x, y);
                newGame.showTheHitPlace(x, y);
                newGame.printOceanMap();
                System.out.println("You Hit " + secondShip.shipName + " Sir !");
                System.out.println("Remaining Missiles : " + (15 - guessesCounter));
            } else if (newGame.thirdShip.contains(givenCoords)) {
                newGame.emptyThatPlace(newGame.thirdShip, x, y);
                newGame.showTheHitPlace(x, y);
                newGame.printOceanMap();
                System.out.println("You Hit " + thirdShip.shipName + " Sir !");
                System.out.println("Remaining Missiles : " + (15 - guessesCounter));
            } else {
                guessesCounter++;
                newGame.showTheNonHitPlace(x, y);
                newGame.printOceanMap();
                System.out.println("You Missed Sir !");
                System.out.println("Remaining Missiles : " + (15 - guessesCounter));
            }

            if (newGame.firstShip.isEmpty() && !firstShip.dead) {
                firstShip.dead = true;
                newGame.playFinalBoomSound();
                System.out.println("Congratulations sir " + firstShip.shipName + " is toasted !");
            } else if (newGame.secondShip.isEmpty() && !secondShip.dead) {
                secondShip.dead = true;
                newGame.playFinalBoomSound();
                System.out.println("Congratulations sir " + secondShip.shipName + " is on fire !");
            } else if (newGame.thirdShip.isEmpty() && !thirdShip.dead) {
                thirdShip.dead = true;
                newGame.playFinalBoomSound();
                System.out.println("Congratulations sir " + thirdShip.shipName + " is Sunken !");
            }
            if (guessesCounter == 15 && (!newGame.firstShip.isEmpty() || !newGame.secondShip.isEmpty() || !newGame.thirdShip.isEmpty())) {
                newGame.playAbortMissionSound();
                System.out.println("Sissi : We are Out Of Missiles Sir");
                System.out.println("General Seal : How did You Join The Navy You Idiot We Lost");
                System.out.println("You : it Was Sissi Not me");

            }
            if (newGame.firstShip.isEmpty() && newGame.secondShip.isEmpty() && newGame.thirdShip.isEmpty()) {
                if (guessesCounter <= 10) {
                    System.out.println("It Took You " + guessesCounter + " to Finish the War");
                    System.out.println("You are a Real Warrior");
                    System.out.println("You : Thank You");
                    newGame.playWiningSound();

                } else {
                    System.out.println("You Did Well After All But You Need More Experience");
                    newGame.playWiningSound();
                }
            }
        }

    }
}
