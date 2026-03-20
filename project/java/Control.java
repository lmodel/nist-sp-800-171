package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  A security requirement
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Control extends IdentifiedElement {

  private List<Parameter> params;

}