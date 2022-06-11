import javax.swing.*;
import java.awt.*;

public class DrawCanvas extends JPanel {
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        setBackground(Color.BLACK);

        g.setColor(Color.CYAN);
        g.drawLine(30, 40, 100, 200);
        g.drawOval(150, 150, 10, 10);
        g.setColor(Color.BLUE);
        g.fillOval(300, 300, 30, 50);
        g.fillRect(400, 350, 60, 50);
        g.setColor(Color.WHITE);
        g.setFont(new Font("Monospaced", Font.PLAIN, 12));
        g.drawString("X0lotl", 10, 20);
    }
}
