package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  An organization-defined parameter for a security requirement
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Parameter extends IdentifiedElement {

  private String usage;
  private List<Guideline> guidelines;

}