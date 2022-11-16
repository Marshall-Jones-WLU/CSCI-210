#include <stdio.h>

/* Define Constants */
//const int NUM_EMPLOYEE = 5;
#define NUM_EMPLOYEE 5
#define OVERTIME_RATE 1.5f
#define STD_WORK_WEEK 40.0f

// struct to store employee data
struct employee
{
    char first_name[20];
    char last_name[20];
    long ident_number;
    float wage;
    float hours;
    float OT;
    float grossPay;
};

// struct to store the total/average/minimum/maximum
struct statistic {
    float hours;
    float OT;
    float grossPay;
};

/* define prototypes here for each function except main */
void Get_Input(struct employee * employeeData, int num_employee)
{
	for (int i=0; i<NUM_EMPLOYEE; ++i){
		printf("Enter hours worked for employee %06ld > ", employeeData[i].ident_number);
		scanf("%f", &employeeData[i].hours);
		if (employeeData[i].hours > 40){
			employeeData[i].OT = employeeData[i].hours - 40;
		}
		else{
			employeeData[i].OT = 0;
		}
	}
}


void Calc_Gross_Pay(struct employee * employeeData, int num_employee)
{
	for (int i=0; i<NUM_EMPLOYEE; ++i){
		employeeData[i].grossPay = (((employeeData[i].hours - employeeData[i].OT) * employeeData[i].wage) +
									(employeeData[i].OT * employeeData[i].wage * OVERTIME_RATE));
	}
}


void Get_Total_and_Avg(struct employee * employeeData, int num_employee, 
						struct statistic * total, 
						struct statistic * average)
{
	for (int i=0; i<NUM_EMPLOYEE; ++i){
		total->hours += employeeData[i].hours;
		total->OT += employeeData[i].OT;
		total->grossPay += employeeData[i].grossPay;
	}
	average->hours = total->hours/NUM_EMPLOYEE;
	average->OT = total->OT/NUM_EMPLOYEE;
	average->grossPay = total->grossPay/NUM_EMPLOYEE;
}


void Get_Min_and_Max(struct employee * employeeData, int num_employee, 
					struct statistic * minimum, 
					struct statistic * maximum)
{
	// Assign minimum variables to first observations in employeeData
	minimum->hours = employeeData[0].hours;
	minimum->OT = employeeData[0].OT;
	minimum->grossPay = employeeData[0].grossPay;
	for (int i=0; i<NUM_EMPLOYEE; ++i){
		// Find minimum and maximum hours
		if (employeeData[i].hours < minimum->hours){
			minimum->hours = employeeData[i].hours;
		}
		else {
			if (employeeData[i].hours > maximum->hours) {
				maximum->hours = employeeData[i].hours;
			}
		}
		// Find minimum and maximum OT
		if (employeeData[i].OT < minimum->OT){
			minimum->OT = employeeData[i].OT;
		}
		else {
			if (employeeData[i].OT > maximum->OT) {
				maximum->OT = employeeData[i].OT;
			}
		}
		// Find minimum and maximum grossPay
		if (employeeData[i].grossPay < minimum->grossPay){
			minimum->grossPay = employeeData[i].grossPay;
		}
		else {
			if (employeeData[i].grossPay > maximum->grossPay) {
				maximum->grossPay = employeeData[i].grossPay;
			}
		}
	}
}


void Print_Results(struct employee * employeeData, int num_employee, 
					struct statistic * total, struct statistic * average, 
					struct statistic * minimum, struct statistic * maximum)
{
	printf("--------------------------------------------------------------------------\n");
	printf("Name\t\tIdent#\t\tWage\t\tHours\tOT\tGross\n");
	printf("--------------------------------------------------------------------------\n");

	for (int i=0; i<NUM_EMPLOYEE; ++i){
		printf("%s %s\t%06ld\t\t%.2f\t\t%.1f\t%.1f\t%.2f\n",
				employeeData[i].first_name,
				employeeData[i].last_name,
				employeeData[i].ident_number,
				employeeData[i].wage,
				employeeData[i].hours,
				employeeData[i].OT,
				employeeData[i].grossPay);
	}
	printf("--------------------------------------------------------------------------\n");
	printf("Total:  \t\t\t\t\t%.1f\t%.1f\t%.2f\n", total->hours, total->OT, total->grossPay);
	printf("Average:\t\t\t\t\t%.1f\t%.1f\t%.2f\n", average->hours, average->OT, average->grossPay);
	printf("Minimum:\t\t\t\t\t%.1f\t%.1f\t%.2f\n", minimum->hours, minimum->OT, minimum->grossPay);
	printf("Maximum:\t\t\t\t\t%.1f\t%.1f\t%.2f\n", maximum->hours, maximum->OT, maximum->grossPay);
}


/* main driver function */
int main()
{
	/* Variable Declaration and initialization */
	struct employee employeeData[NUM_EMPLOYEE] = {
		{"John", "Smith", 98401, 15.20},
		{"Mary", "Loo", 526488, 9.15},
    	{"Frank", "Lee", 765349, 10.30},
    	{"Jeff", "Walters", 34645, 12.35},
    	{"Julie", "Winston", 127615, 13.10}
	};

	struct statistic total, average, minimum, maximum;

	/* Call various functions needed to reading, calculating, and printing as needed */
	Get_Input(employeeData, NUM_EMPLOYEE);
	Calc_Gross_Pay(employeeData, NUM_EMPLOYEE);
	
	/* Function call to output results to the screen in table format. */
	Get_Total_and_Avg (employeeData, NUM_EMPLOYEE, &total, &average);
	Get_Min_and_Max(employeeData, NUM_EMPLOYEE, &minimum, &maximum);
	Print_Results (employeeData, NUM_EMPLOYEE, &total, &average, &minimum, &maximum);
	
	return(0);
};


/* other functions */








