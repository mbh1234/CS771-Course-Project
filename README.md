#### **Project Overview**

This repository contains the implementation and documentation of the **Companion Arbiter Physical Unclonable Function (CAR-PUF)**, an advanced PUF designed to enhance hardware security by leveraging unique manufacturing variations in Integrated Circuits (ICs). The CAR-PUF builds upon the traditional Arbiter PUF by introducing a companion structure, significantly increasing resistance to modeling attacks and enhancing overall system robustness.  

---

#### **CAR-PUF Definition and Working**

1. **Basic Structure**  
   - **Arbiter PUF**: Consists of multiple delay paths configured in pairs. A final arbiter determines which signal arrives first based on unique delay characteristics, inherently tied to the manufacturing variability of ICs.  
   - **Companion PUF**: Enhances the traditional Arbiter PUF by adding a secondary processing layer, such as an XOR function or another delay-based PUF. This interaction makes the CAR-PUF output less predictable and significantly harder for attackers to model.  

2. **Challenge-Response Mechanism**  
   - **Challenge**: A binary input stream that configures the delay paths. The length of the challenge determines system complexity.  
   - **Response**: The arbiter produces a binary output based on delay differences. In CAR-PUF, the companion structure processes this response further, increasing its complexity and unpredictability.  

3. **Applications**  
   - **Authentication**: Secure authentication protocols using challenge-response pairs as cryptographic keys.  
   - **Key Generation**: Generation of unique cryptographic keys tied to each device.  
   - **Hardware Security**: Protection against counterfeiting and unauthorized access to hardware systems.  

4. **Advantages**  
   - **Enhanced Security**: The companion structure adds robustness and resistance to modeling attacks.  
   - **Scalability**: Adaptable for implementation in various ICs and applications.  
   - **Efficiency**: Designed for low power consumption, suitable for constrained devices.  

5. **Challenges**  
   - **Complex Design**: Increased design complexity due to the companion mechanism.  
   - **Environmental Sensitivity**: Responses may be affected by variations in temperature and voltage, requiring careful calibration.  

---

#### **Repository Structure**

```
├── model.py                 # Python implementation of the CAR-PUF model
├── train.dat                # Training dataset for CAR-PUF
├── test.dat                 # Testing dataset for CAR-PUF
├── Final Report.pdf         # Detailed project report covering methodology, results, and analysis
├── Problem Statement.pdf    # Original problem statement for the CAR-PUF project
└── README.md                # Project documentation
```

---

#### **Setup and Usage**

1. **Prerequisites**  
   - Python 3.x  
   - Libraries: NumPy, Matplotlib, and other standard data science libraries.  

2. **Steps to Run**  
   - Clone the repository:  
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```  
   - Ensure the `train.dat` and `test.dat` files are in the same directory as `model.py`.  
   - Run `model.py` to train and evaluate the CAR-PUF model:  
     ```bash
     python model.py
     ```  

3. **Expected Output**  
   - The script processes the datasets and provides metrics for the CAR-PUF's performance, including reliability and unpredictability of responses.

---

#### **Documentation**
- **Final Report**: A comprehensive analysis of CAR-PUF's design, implementation, and experimental results.  
- **Problem Statement**: Outlines the objectives and challenges of the project.  

---

#### **Acknowledgements**
This project uses the concept of Arbiter PUFs, extending their functionality through innovative companion mechanisms for enhanced hardware security. 
