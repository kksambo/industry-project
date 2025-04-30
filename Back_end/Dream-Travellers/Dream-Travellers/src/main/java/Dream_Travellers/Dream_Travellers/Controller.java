package Dream_Travellers.Dream_Travellers;

import java.util.ArrayList;
import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import Dream_Travellers.Dream_Travellers.models.CustomerMessage;

@RestController
@CrossOrigin("*")
public class Controller {


public CustomerMessage newMessage(String customerName,String customerContact, String message){


return new CustomerMessage(customerName, customerContact, message);

}



@GetMapping("/mapula")
    public String myMessage(){

    return newMessage("Mapula", "05487693", "The page is not working properly").toString();


    }

@GetMapping("/myList")
public List<CustomerMessage> getAllMessages(){


 List<CustomerMessage> list=new ArrayList<>();

 list.add( newMessage("Mapula", "05487693", "The page is not working properly"));
 list.add( newMessage("Mapula", "05487693", "The page is not working properly"));
 list.add( newMessage("Mapula", "05487693", "The page is not working properly"));
 list.add( newMessage("Mapula", "05487693", "The page is not working properly"));
    
    return list;
  } 
  
  

@PostMapping("/messages")
  public ResponseEntity<CustomerMessage> getSendMessages(@RequestBody CustomerMessage message){


    message.setId(Long.parseLong("200"));
    return ResponseEntity.ok(message);

  }
    
}
