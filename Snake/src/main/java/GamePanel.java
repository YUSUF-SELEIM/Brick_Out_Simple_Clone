//game panel will extend from jpanel and implements actionlistener

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.JPanel;
import javax.swing.Timer;

// the GamePanel contains all the code of the game
public class GamePanel extends JPanel implements ActionListener { /// implementing actionListener methods (Forced) as it is an interface 

    File file = new File("theme.wav");
    AudioInputStream ASM = AudioSystem.getAudioInputStream(file);
    Clip clipM = AudioSystem.getClip();
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT = 600;
    static final int UNIT_SIZE = 25; /// how big are the objects in the game panel (here each item has 25 width and height)
    static final int GAME_UNITS = (SCREEN_WIDTH * SCREEN_HEIGHT) / UNIT_SIZE; // how many objects can be fitted in the panel
    static final int DELAY = 100; // how fast is the game --> the higher the number the slowest is the game
    final int x[] = new int[GAME_UNITS];  // this array will contain all body parts (units) of the snake found on X-axis including his head
    final int y[] = new int[GAME_UNITS]; // this array will contain all body parts (units) of the snake found on Y-axis including his head
    int initial_BodyParts = 6;  // the game begins with a snake of length 6 units
    int applesEaten;
    char initial_Direction = 'R';
    boolean running = false;
    Timer timer;    // object of class Timer
    Random random;  // object of class Random

    class Apple {

        int X, Y;
    }; // anonymous class just 1 object can be created

    Apple apple = new Apple();

    GamePanel() throws UnsupportedAudioFileException, IOException, LineUnavailableException { // this here refers the object of class panel    
        clipM.open(ASM);
        clipM.loop(5000);
        random = new Random();
        // Dimension dimension = new Dimension();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.black);
        this.setFocusable(true); /// unknown yet
        //  MyKeyAdapter myKeyAdapter = new MyKeyAdapter();
        this.addKeyListener(new MyKeyAdapter());
        ///////////////constructing the game panel is done here the next thing we will call startGame() Method \\\\\\\\\\\\\\\\\\\\
        startGame();
    }

    public void startGame() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        newApple();
        running = true;
        timer = new Timer(DELAY, this); // the timer of class swing takes int and actionListener as an args /// the timer of class utility takes string as an args
        //this refers to the object created from GamePanel class that implements the ActionListener Interface
        timer.start();
        clipM.start();
        clipM.loop(50000);
    }

    @Override //from JComponent superclass
    public void paintComponent(Graphics g) { // input is an object of class Graphics
        super.paintComponent(g);
        try {
            draw(g);
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException ex) {
            Logger.getLogger(GamePanel.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

//draws all drawable things in the game
    public void draw(Graphics g) throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        ///drawing main menu
        if (running) {
            //   playSoundTheme();
            //this forloop draws lines across X-axis --> the space etween them is equal to the UNIT_SIZE
//            for (int i = 0; i < SCREEN_HEIGHT / UNIT_SIZE; i++) {
//                g.drawLine(i * UNIT_SIZE, 0, i * UNIT_SIZE, SCREEN_HEIGHT); // X-axis Lines
//                g.drawLine(0, i * UNIT_SIZE, SCREEN_WIDTH, i * UNIT_SIZE); // Y-axis Lines
//                //y1 --> SCREEN_HEIGHT or SCREEN_WIDTH
//            }
            ///drawing the apple
            g.setColor(Color.red);
            g.fillOval(apple.X, apple.Y, UNIT_SIZE, UNIT_SIZE);
            /// drawing the snake
            for (int i = 0; i < initial_BodyParts; i++) {
                if (i == 0) {// snake 's head
                    g.setColor(Color.yellow);
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                } else {// the rest of his body
                    g.setColor(Color.green);
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
            }
/// the next thing is that we need to move the snake
        } else { // gameOver
            clipM.stop();
            clipM.flush();
            clipM.setFramePosition(0);
            gameOver(g);
            playSoundGameOver();
        }
    }
/// this method randomly generates the coordinates of the a new apple each time the snake eats one

    public int highestScore() {
        int max = 0;
        if (max < applesEaten) {
            max = applesEaten;
        }
        return max;
    }

    public void newApple() {
        apple.X = random.nextInt((int) SCREEN_WIDTH / UNIT_SIZE) * UNIT_SIZE; //(24) the division by unit_size is done so that each apple will take only one square(unit size)
        apple.Y = random.nextInt((int) SCREEN_HEIGHT / UNIT_SIZE) * UNIT_SIZE;
    }

    public void move() { // when the snake moves the each index in the array is shifted by one unit_size in a specified direction
        for (int i = initial_BodyParts; i > 0; i--) {
            x[i] = x[i - 1];
            y[i] = y[i - 1];
        }

        for (int i = 0; i < initial_BodyParts; i++) {
            if (x[i] < 0) {
                x[i] = SCREEN_WIDTH; //Warp to right
            } else if (x[i] >= SCREEN_WIDTH) {
                x[i] = 0; //Warp to left
            }

            if (y[i] < 0) {
                y[i] = SCREEN_HEIGHT; //Warp to bottom
            } else if (y[i] >= SCREEN_HEIGHT) {
                y[i] = 0; //Warp to top
            }
        }
        switch (initial_Direction) { /// it goes logically with a normal graph imagine an x-axis with y axis it is inverted
            case 'U':
                y[0] = y[0] - UNIT_SIZE;
                break;
            case 'D':
                y[0] = y[0] + UNIT_SIZE;
                break;
            case 'L':
                x[0] = x[0] - UNIT_SIZE;
                break;
            case 'R':
                x[0] = x[0] + UNIT_SIZE;
                break;
            default:
                break;
        }

    }

    public void playSoundAppleEaten() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("eat.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void playSoundGameOver() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        File file = new File("GameOver.wav");
        AudioInputStream AS = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(AS);
        clip.start();
    }

    public void checkApple() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        if ((x[0] == apple.X) && (y[0] == apple.Y)) {
            initial_BodyParts = initial_BodyParts + 1;
            applesEaten++;
            newApple();
            playSoundAppleEaten();
        }
    }

    public void checkCollisions() {
        for (int i = initial_BodyParts; i > 0; i--) {
            if ((x[0] == x[i]) && (y[0] == y[i])) { // if the head collided  with the body
                running = false;
            }
        }
        ////Border Collisions
//        if (x[0] < 0) { //collision of head with the left-Border
//            running = false;
//        }
//        if (x[0] > SCREEN_WIDTH) { // collision of head with right-Border
//            running = false;
//        }
//        if (y[0] < 0) { // collision of head with top-Border
//            running = false;
//        }
//        if (y[0] > SCREEN_HEIGHT) { // collision of head with bottom-Border
//            running = false;
//        }
//
        if (running == false) { // (!running)
            timer.stop();
        }
    }

    public void restartMessageDisplay(Graphics g) {
        String restartMessage = " Press Enter to Try Again ";
        g.setFont(new Font("", Font.BOLD, 40));
        FontMetrics metrics = getFontMetrics(g.getFont());
        g.drawString(restartMessage, (SCREEN_WIDTH - metrics.stringWidth(restartMessage)) / 2, (SCREEN_HEIGHT - 50));

    }

    public void gameOver(Graphics g) {  // any method that modifies the panel it requires input of object from class graphics
        ///////////////////////////////////////////////////displaying score\\\\\\\\\\\\\\\\\\\\\\\
        g.setColor(Color.red);
        // Font font = new Font();
        g.setFont(new Font("", Font.BOLD, 40));
        FontMetrics metrics1 = getFontMetrics(g.getFont()); // aligns text in the center of the screen
        g.drawString("Score : " + applesEaten, (SCREEN_WIDTH - metrics1.stringWidth("Score : " + applesEaten)) / 2, g.getFont().getSize()); // puts the text in the center
        //////////////////////////////////displaying game over \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\F
        g.setColor(Color.red);
        // Font font = new Font();
        g.setFont(new Font("", Font.BOLD, 75));
        FontMetrics metrics2 = getFontMetrics(g.getFont()); // aligns text in the center of the screen
        g.drawString("Game Over", (SCREEN_WIDTH - metrics2.stringWidth("Game Over")) / 2, SCREEN_HEIGHT / 2); // puts the text in the center
        restartMessageDisplay(g);
    }

    @Override /// moving the snake is done here
    public void actionPerformed(ActionEvent e) {
        if (running) {
            try {
                move();
                checkApple();
                checkCollisions();

            } // game is no longer running game over
            catch (UnsupportedAudioFileException | IOException | LineUnavailableException ex) {
                Logger.getLogger(GamePanel.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        repaint(); ///The paintComponent() method can also be called explicitly by the repaint() method defined in Component class

    }

//// this inner class is responsible about all the controls taken from the keyboard in game
    public class MyKeyAdapter extends KeyAdapter {
//// keyPressed method and it's args is overriden from KeyAdapter Class

        @Override
        public void keyPressed(KeyEvent e) {
            switch (e.getKeyCode()) {
                case KeyEvent.VK_LEFT:
                    if (initial_Direction != 'R') { // this block of if prevents the snake from turning 180 degree so as long as the direction is not R didnot turn then let the snake go left
                        initial_Direction = 'L';
                    }
                    break;
                case KeyEvent.VK_RIGHT:
                    if (initial_Direction != 'L') { // this block of if prevents the snake from turning 180 degree so as long as the direction is not R didnot turn then let the snake go left
                        initial_Direction = 'R';
                    }
                    break;
                case KeyEvent.VK_UP:
                    if (initial_Direction != 'D') { // this block of if prevents the snake from turning 180 degree so as long as the direction is not R didnot turn then let the snake go left
                        initial_Direction = 'U';
                    }
                    break;
                case KeyEvent.VK_DOWN:
                    if (initial_Direction != 'U') { // this block of if prevents the snake from turning 180 degree so as long as the direction is not R didnot turn then let the snake go left
                        initial_Direction = 'D';
                    }
                    break;

                case KeyEvent.VK_P:
                    timer.stop();
                    clipM.stop();
                    break;

                case KeyEvent.VK_S:
                    timer.start();
                    clipM.start();
                    break;
                //game restart
                case KeyEvent.VK_ENTER:

                    if (!running) {
                        running = true;

                        initial_BodyParts = 6;
                        applesEaten = 0;
                        try {
                            startGame();
                        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException ex) {
                            Logger.getLogger(GamePanel.class.getName()).log(Level.SEVERE, null, ex);
                        }
                        repaint();
                    }
                    break;
            }
        }
    }
}
