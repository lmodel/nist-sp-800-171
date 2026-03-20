package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  Selection constraints specifying allowed values for a parameter
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParameterSelection  {

  private String how-many;
  private List<String> choice;

}