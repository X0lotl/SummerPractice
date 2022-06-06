#include <graphics.h>
#include <conio.h>
#include <math.h>
float F1(float z)
{
    return 2*sin(2*z) + 1;
}

float F2(float z)
{
    return pow((z+5),3)*(1+sin(z)*sin(z));
}

void main()
{
    int g = DETECT, r, k, a=0, n=200, xg, yg;
    float b=3.14, x, dx, Mx, M1, M2;
    initgraph(&g, &r, "D:\\Borlandc\\BGI\0");
    setgraphmode(2);
    setbkcolor(0);
    outtextxy(630,245,"X");
    outtextxy(15,10,"Y");
    setcolor(7);
    moveto(0, 240);
    linerel(640, 0);
    setcolor(7);
    line(10, 0, 10, 480);
    setcolor(7);
    getch();
    Mx=625/3.14;
    M1=235/3.0;
    M2=235/624.0;
    dx=fabs((b-a)/(n-1));
    x=a;
    moveto(10, floor(M1*F1(0)) + 240);
    for(int i=1; i<=n; i++, x+=dx)
    {
        xg = floor(Mx*x);
        yg = floor(M1*F1(x));
        lineto(xg + 10, yg + 240);
    }
    settextstyle(0, 0, 1);
    outtextxy(470, 150, "F1=2*sin(2*x)+1");
    getch();
    x=a;
    setcolor(7);
    moveto(10, floor(M2*F2(0)) + 240);
    for(i=1; i<=n; i++, x+=dx)
    {
        xg = floor(Mx*x);
        yg = floor(M2*F2(x));
        lineto(xg + 10, yg + 240);
    }
    settextstyle(0, 0, 1);
    outtextxy(310, 430, "F2=((x+5)^3)*(1+sin^2(x))");
    getch();
    closegraph();
}