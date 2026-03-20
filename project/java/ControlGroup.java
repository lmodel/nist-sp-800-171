package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  A family group of security requirements
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlGroup extends IdentifiedElement {

  private List<Control> controls;

}