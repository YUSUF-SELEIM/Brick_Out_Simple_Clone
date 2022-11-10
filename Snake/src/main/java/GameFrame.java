///gmae frame class will extend from jframe class

import java.io.IOException;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.JFrame;

public class GameFrame extends JFrame {

    GameFrame() throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        GamePanel panel = new GamePanel(); // when GameFrame constructor is invoked an object of GamePanel is Created (the Frame contains the panel)
        this.add(panel); //this here refers to GameFrame Object (panel object is added to the frame object)
        this.setTitle("Snake Game V.1.1");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack(); /// fits the frame around all the components added to the frame
        this.setVisible(true); /// window is shown
        this.setLocationRelativeTo(null); /// makes the window appear in the middle of the screen

    }
}
