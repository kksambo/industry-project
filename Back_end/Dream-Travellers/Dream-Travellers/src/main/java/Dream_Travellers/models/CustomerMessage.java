package Dream_Travellers.Dream_Travellers.models;

import java.util.Date;

public class CustomerMessage {

    private Long id;
    private String customerName;
    private String customerContact;
    private String message;
    private Date date;

    public CustomerMessage(String customerName,String customerContact, String message){
        this.customerName=customerName;
        this.customerContact=customerContact;
        this.message=message;
        this.date=new Date();
        
    }

    public String getCustomerName(){
     return this.customerName;
    }
    public String getCustomerContact(){
        return customerContact;
       }
       public String getMessage(){
        return message;
       }
       public Date getDate(){
        return date;
       }
       public Long getId(){
        return id;
       }

    public void setCustomerName(String customerName){
        this.customerName=customerName;
    }
    public void setCustomerContact(String customerContact){
            this.customerContact=customerContact;
    }
    public void setMessage(String message){
        this.message=message;
    }
    public void setId(Long id){
        this.id=id;
    }

public String toString(){


String out = "{<br>customerName:"+customerName+",<br>customerContact:"+customerContact+",<br>message:" +message +",<br>id:"+id+",<br>date:"+date+"}";





return out;
}

}
