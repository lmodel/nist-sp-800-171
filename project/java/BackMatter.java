package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  OSCAL back-matter section
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BackMatter  {

  private List<Resource> resources;

}