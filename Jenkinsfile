pipeline{
  agent any
  stages{
    stage("Build Docker Image"){
      steps{
        echo "Build the Docker Image"
        bat "docker build -t myapp"
      }
    }
    stage('Run the Image'){
      steps{
        echo "Run the Docker Image"
        bat "docker rm -f mycontainer || exit 0"
        bat "docker run -d -p 5001:5001 mycontainer myapp"
      }
    }
  }
}
        
        
        
    
          
