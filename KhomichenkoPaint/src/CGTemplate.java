import javax.swing.*;
import java.awt.*;

public class CGTemplate extends JFrame {
    public static final int CANVAS_WIDTH = 1024;
    public static final int CANVAS_HEIGHT = 720;

    private DrawCanvas canvas;

    public CGTemplate() {
        canvas = new DrawCanvas();
        canvas.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));

        Container cp = getContentPane();
        cp.add(canvas);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
        setTitle("Test");
        setVisible(true);
    }
}
