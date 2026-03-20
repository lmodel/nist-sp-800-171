package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  A name-value property with optional namespace
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Property  {

  private String name;
  private String value;
  private String ns;
  private String class;

}