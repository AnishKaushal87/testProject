public class DataProcessor {

public void processData(List dataList) {

class Validator {

void validate(Data data) {

if (data == null || data.getValue() == null) {

throw new IllegalArgumentException("Invalid data");

}

}

}
```
    class Transformer {
        Data transform(Data data) {
            data.setValue(data.getValue().toUpperCase());
            return data;
        }
    }
    Validator validator = new Validator();
    Transformer transformer = new Transformer();
    
    for (Data data : dataList) {
        validator.validate(data);
        data = transformer.transform(data);
        saveData(data);
    }
}
private void saveData(Data data) {
    // Save data to database
    Database db = new Database();
    db.connect();
    db.save(data);
    db.disconnect();
}
```

}