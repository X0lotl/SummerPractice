import javax.swing.*;
import java.awt.*;

public class Paint {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new CGTemplate();
            }
        });
    }
}
