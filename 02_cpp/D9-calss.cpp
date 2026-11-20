// CLASSES
// identiy is object location
// constructor / destructor --> create and destroy container
// access specifier
//   public, private, protected
// four pillars of oops C++
//  

// 1, Abstraction 
//  hides impemnation  - use without knownbackgroudn
//  improveds maintainab9ility
//  enhacnes flexibility 

// Inheritance types: - single multiple , multilevel inheritance 

 #include <bits/stdc++.h>
#include <math.h>

using namespace std;

class shapes{
    public:
        virtual void area(){
            cout << "Every shape has their own specific area" << endl;
            return; // only for void function
        }   
         void perimeter(){  // Since it s not virtual then it wont be overridden
            cout << "Every shape has some perimeter:" << endl;
        }

};

//Inheritance -- can fetch teh feature
//Polymorphism - one shape can have diff features

class circle : public shapes { 
    public:
        double r;
        circle(double r):r(r) {};
    
        void area() override{ // polymorphism 
            cout << "Circle's area is: " << 3.14*r*r << endl;
            return;
        }
        void perimeter(){
          cout << " Circl's perimeter is " << 2*3.14*r << endl;
            return;
        }
};

// class triangle : public shapes {
//     public:
//         int l,b ;
//         void area() override{
//             cout << "triangle's area is: " << 0.5 * l * b << endl;
//             return;
//         };
//         void perimeter(){
//           cout << " Triangle's perimeter is " << l + b + (pow(pow(b, 2) + pow(l, 2)),0.5) << endl;
//         };
// };
    
int main(){
    shapes *spt = new circle(3);
    spt->area();
    spt->perimeter();
  //  delete spt();
    return 0;
    
}