//Raul Diaz
//Homework #1

#include "ccc_win.h"

using namespace std;

class Parachutist
{
public:
  Parachutist();                            //constructors
  Parachutist(Point loc);
  void display_close();
  void display_open();
  void move(double dx, double dy);
private:
  double sec;
  Point p;
  void Parachuteoff() const;                 //accessors
  void Parachuteon() const;
};

Parachutist::Parachutist()
{
  p = Point(0,0);
}


Parachutist::Parachutist(Point loc)
{
  p=loc;
}


void Parachutist::display_close()
{
     Parachuteoff();
}


void Parachutist::display_open()
{
     Parachuteon();
}


void Parachutist:: move(double dx, double dy)
{
 p.move(dx, dy);
}



void Parachutist::Parachuteoff() const
{
  double x=p.get_x();
  double y=p.get_y();
    //head
  Point h1(x,y);
    //body
  Point n1(x, y-20);			//top of neck / bottom of head
  Point b1(x, y-30);			//top of body / bottom of neck
  Point b2(x, y-65);			//bottom of body
  Point la(x-30, y-20);			//left arm
  Point ra(x + 30, y-20);		//right arm
  Point ll(x - 20, y - 100);	//left leg
  Point rl(x + 20, y - 100);	//right leg

  cwin << Circle(h1, 20) << Line(n1, b2) << Line(b1, la) << Line(b1, ra) << Line(b2, ll) << Line(b2, rl);
}



void Parachutist::Parachuteon() const
{
  double x=p.get_x();
  double y=p.get_y();
    //head
  Point h1(x,y);
  //body
  Point n1(x, y - 20);			//top of neck / bottom of head
  Point b1(x, y - 30);			//top of body / bottom of neck
  Point b2(x, y - 65);			//bottom of body
  Point la(x - 30, y - 20);		//left arm
  Point ra(x + 30, y - 20);		//right arm
  Point ll(x - 20, y - 100);	//left leg
  Point rl(x + 20, y - 100);	//right leg
    //parachute
  //Point n1(x, y-20);
  Point s1(x-60, y+65);
  Point s2(x+60, y+65);
  Point p2(x, y+100);
    //connect the dots
  cwin << Circle(h1,20) << Line(n1, b2) << Line(b1, la) << Line(b1, ra) << Line(b2, ll) << Line(b2, rl) << Line(b1,s1) << Line (b1,s2) << Line(s1,s2) << Line(s1,p2) << Line(s2,p2);
}


int ccc_win_main()
{
  double x = 50;           //starting point x coordinate
  double y = 950;          //starting point y coordinate
  double velocity = 0;
  double drag = 0;
  double sec = 0;
  double speed = 100;        //plane speed
  double openchute = 6;      //seconds at which chute pulled (or openchute time)
  cwin.coord(0,1000,1000,0);  

  Parachutist fall(Point(x,y));

  while (y > 0)         
  {
    if(sec < openchute)
    {
      sec++;
      fall.display_close();
      velocity = 32*sec;                    
      drag = speed;
      if(velocity > 174) {velocity = 174;}    //doesn't go over terminal velocity
      fall.move(drag,-velocity);              //change y's position  //change x's position
    }
    else if(sec >= openchute)
    {
      sec++;
      fall.display_open();
      velocity = velocity-(100 * sec);
      drag = drag-20;                 
      if(drag <= 0)  {drag = 0;}              //don't want them going backwards
      if(velocity <= 17) {velocity = 17;}     //Slowest parachute will slow them down.
      fall.move(drag,-velocity);              //change y's position  //change x's position  
    }  
    
	y = y - velocity;
  }
  return 1; 
}
