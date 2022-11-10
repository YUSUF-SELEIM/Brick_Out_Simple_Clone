//ღ(¯`◕‿◕´¯) ♫ ♪ ♫ YuSuF ♫ ♪ ♫ (¯`◕‿◕´¯)ღ

import java.io.*;
import java.util.*;
import javax.sound.sampled.*;

public class game {
// creation of ships is here

    int ROWS = 10;
    int COLUMNS = 10;
    String[][] GRID = new String[ROWS][COLUMNS];
    Random random = new Random();
    ArrayList<String> firstShip = new ArrayList<>();
    ArrayList<String> secondShip = new ArrayList<>();
    ArrayList<String> thirdShip = new ArrayList<>();

    public void playBoomSound() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("boom.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void playWiningSound() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("win.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void playRogerThatSound() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("Roger-that.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void playFinalBoomSound() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("finalboom.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void playAbortMissionSound() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("abort.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void createOceanMap() {
        //Top section of Ocean Map
        System.out.print("  ");
        for (int i = 0; i < COLUMNS; i++) {
            System.out.print(i);
        }
        System.out.println();

        //Middle section of Ocean Map
        for (int i = 0; i < GRID.length; i++) { //numRows
            for (int j = 0; j < GRID[i].length; j++) { //numCols
                GRID[i][j] = " ";
                if (j == 0) {
                    System.out.print(i + "|" + GRID[i][j]);
                } else if (j == GRID[i].length - 1) {
                    System.out.print(GRID[i][j] + "|" + i);
                } else {
                    System.out.print(GRID[i][j]);
                }
            }
            System.out.println();
        }

        //Bottom section of Ocean Map
        System.out.print("  ");
        for (int i = 0; i < COLUMNS; i++) {
            System.out.print(i);
        }
        System.out.println();
    }

    public void printOceanMap() {
        System.out.println();
        //First section of Ocean Map
        System.out.print("  ");
        for (int i = 0; i < COLUMNS; i++) {
            System.out.print(i);
        }
        System.out.println();

        //Middle section of Ocean Map
        for (int x = 0; x < ROWS; x++) {
            System.out.print(x + "|");

            for (int y = 0; y < COLUMNS; y++) {
                System.out.print(GRID[x][y]);
            }

            System.out.println("|" + x);
        }

        //Last section of Ocean Map
        System.out.print("  ");
        for (int i = 0; i < COLUMNS; i++) {
            System.out.print(i);
        }
        System.out.println();
    }

    boolean emptyOrNot(int row, int column, int shipLength, boolean verticalOrHorizontal, boolean upOrDown, boolean rightOrLeft) {
        if (verticalOrHorizontal) {
            if (upOrDown) {
                for (int i = row; i >= (Math.abs(shipLength - (row + 1))); i--) {
                    if (!" ".equals(GRID[i][column])) {
                        return false;
                    }

                }
            } else {
                for (int i = row; i <= (shipLength + (row - 1)); i++) {
                    if (!" ".equals(GRID[i][column])) {
                        return false;
                    }

                }
            }
        } else {
            if (rightOrLeft) { //right
                for (int i = column; i <= (shipLength + (column - 1)); i++) {
                    if (!" ".equals(GRID[row][i])) {
                        return false;
                    }

                }
            } else {
                for (int i = column; i >= (Math.abs(shipLength - (column + 1))); i--) {
                    if (!" ".equals(GRID[row][i])) {
                        return false;
                    }

                }
            }
        }
        return true;
    }

    void filingTheFirstShipArray(int row, int column) {
        String temp = row + "" + column;
        firstShip.add(temp);
    }

    void filingTheSecondShipArray(int row, int column) {
        String temp = row + "" + column;
        secondShip.add(temp);
    }

    void filingTheThirdShipArray(int row, int column) {
        String temp = row + "" + column;
        thirdShip.add(temp);
    }

    void computerDeployingShips(int shipLength, int shipNo) {
        MAIN:
        while (true) {
            int row = random.nextInt(9) + 1;
            int column = random.nextInt(9) + 1;
            boolean verticalOrHorizontal = random.nextBoolean();
            boolean upOrDown = random.nextBoolean();
            boolean rightOrLeft = random.nextBoolean();
            if (verticalOrHorizontal) { //vertical
                if (upOrDown) { //up
                    if (row - shipLength >= 0 && " ".equals(GRID[row][column])) {
                        if (emptyOrNot(row, column, shipLength, verticalOrHorizontal, upOrDown, rightOrLeft)) {
                            for (int i = row; i >= (Math.abs(shipLength - (row + 1))); i--) {
                                // GRID[i][column] = "X";
                                if (shipNo == 1) {
                                    filingTheFirstShipArray(i, column);
                                } else if (shipNo == 2) {
                                    filingTheSecondShipArray(i, column);
                                } else {
                                    filingTheThirdShipArray(i, column);
                                }
                            }
                        } else {
                            continue MAIN;
                        }
                        break;
                    } else {
                        continue MAIN;
                    }
                } else {
                    if (row + shipLength <= 9 && " ".equals(GRID[row][column])) { // down
                        if (emptyOrNot(row, column, shipLength, verticalOrHorizontal, upOrDown, rightOrLeft)) {
                            for (int i = row; i <= (shipLength + (row - 1)); i++) {
                                //GRID[i][column] = "X";
                                if (shipNo == 1) {
                                    filingTheFirstShipArray(i, column);
                                } else if (shipNo == 2) {
                                    filingTheSecondShipArray(i, column);
                                } else {
                                    filingTheThirdShipArray(i, column);
                                }
                            }
                        } else {
                            continue MAIN;
                        }
                        break;
                    } else {
                        continue MAIN;
                    }
                }
            } else { //Horizontal
                if (rightOrLeft) { //right
                    if (column + shipLength <= 9 && " ".equals(GRID[row][column])) {
                        if (emptyOrNot(row, column, shipLength, verticalOrHorizontal, upOrDown, rightOrLeft)) {
                            for (int i = column; i <= (shipLength + (column - 1)); i++) {
                                // GRID[row][i] = "X";
                                if (shipNo == 1) {
                                    filingTheFirstShipArray(row, i);
                                } else if (shipNo == 2) {
                                    filingTheSecondShipArray(row, i);
                                } else {
                                    filingTheThirdShipArray(row, i);
                                }
                            }
                        } else {
                            continue MAIN;
                        }
                        break;
                    } else {
                        continue MAIN;
                    }
                } else {
                    if (column - shipLength >= 0 && " ".equals(GRID[row][column])) {
                        if (emptyOrNot(row, column, shipLength, verticalOrHorizontal, upOrDown, rightOrLeft)) {
                            for (int i = column; i >= (Math.abs(shipLength - (column + 1))); i--) {
                                // GRID[row][i] = "X";
                                if (shipNo == 1) {
                                    filingTheFirstShipArray(row, i);
                                } else if (shipNo == 2) {
                                    filingTheSecondShipArray(row, i);
                                } else {
                                    filingTheThirdShipArray(row, i);
                                }
                            }
                        } else {
                            continue MAIN;
                        }
                        break;
                    } else {
                        continue MAIN;
                    }
                }
            }

        }
    }

    void showTheHitPlace(int x, int y) throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        if (" ".equals(GRID[x][y])) {
            GRID[x][y] = "X";
            playBoomSound();
        }
    }

    void showTheNonHitPlace(int x, int y) {
        if (" ".equals(GRID[x][y])) {
            GRID[x][y] = "@";
        }
    }

    void emptyThatPlace(ArrayList<String> ar, int x, int y) {
        GRID[x][y] = " ";
        ar.remove(x + "" + y);
    }

    void welcomeSir() {
        System.out.println("<< Welcome To Sink The Ship Game >>");
        System.out.println("Computer is Deploying it's Ships.....");
        System.out.println("Now,Here's The Mortar Man sissi");
        System.out.println("He's Here to Help You to Hit The Enemy Ships");
        System.out.println("Give Him The Coords of The Place You Want to Hit >>");
        System.out.println("sissi : I'm Ready Sir , I'm On Your Mark");
        System.out.println("_We Have 15 Missiles in our Arsenal_");
        System.out.println("Here's The Map Good Luck !");
        createOceanMap();
    }
}
