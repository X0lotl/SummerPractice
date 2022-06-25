import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;

public class Paint{
    //HashMap<JButton, Color> colorButtons = new HashMap<>();
    JButton clearBtn, blackBtn, blueBtn, greenBtn, redBtn, magentaBtn;
    DrawArea drawArea;
    ActionListener actionListener = new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == clearBtn) {
                drawArea.clear();
            } else if (e.getSource() == blackBtn) {
                drawArea.black();
            } else if (e.getSource() == blueBtn) {
                drawArea.blue();
            } else if (e.getSource() == redBtn) {
                drawArea.red();
            } else if (e.getSource() == magentaBtn) {
                drawArea.magenta();
            } else if (e.getSource() == greenBtn) {
                drawArea.green();
            }
        }
    };

    public static void main(String[] args) {
        new Paint().show();
    }

    public void show() {
        JFrame frame = new JFrame("MyPaint");
        Container content = frame.getContentPane();
        content.setLayout(new BorderLayout());

        drawArea = new DrawArea();

        content.add(drawArea, BorderLayout.CENTER);

        JPanel controls = new JPanel();

        clearBtn  = new JButton("Clear");
        clearBtn.addActionListener(actionListener);

        blackBtn = new JButton("Black");
        blackBtn.addActionListener(actionListener);

        blueBtn = new JButton("Blue");
        blueBtn.addActionListener(actionListener);

        greenBtn = new JButton("Green");
        greenBtn.addActionListener(actionListener);

        redBtn = new JButton("Red");
        redBtn.addActionListener(actionListener);

        magentaBtn = new JButton("Magenta");
        magentaBtn.addActionListener(actionListener);

        controls.add(greenBtn);
        controls.add(blackBtn);
        controls.add(blueBtn);
        controls.add(redBtn);
        controls.add(magentaBtn);
        controls.add(clearBtn);

        content.add(controls, BorderLayout.SOUTH);

        frame.setSize(600, 600);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
