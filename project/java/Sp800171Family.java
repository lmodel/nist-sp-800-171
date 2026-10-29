package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  One of the seventeen families that SP 800-171 Revision 3 sorts its security requirements into, such as Access Control (03.01) or Supply Chain Risk Management (03.17).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171Family  {

  private String title;
  private String description;
  private String familyNumber;
  private List<Sp800171Requirement> familyRequirements;

}