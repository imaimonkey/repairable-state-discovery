# V2R cluster inventory

2026-09-25T07:42:19.740544+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318863015936 available bytes; 82.21% used; 112480363 free inodes.

server1 `/home`: 318863015936 available bytes; 82.21% used; 112480363 free inodes.

server1 `/tmp`: 318863015936 available bytes; 82.21% used; 112480363 free inodes.

server1 `/var/tmp`: 318863015936 available bytes; 82.21% used; 112480363 free inodes.

server1 `/mnt/raid5`: 399605796864 available bytes; 98.17% used; 337558310 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22852280320 available bytes; 98.73% used; 110410509 free inodes.

server2 `/home`: 22852280320 available bytes; 98.73% used; 110410509 free inodes.

server2 `/tmp`: 22852280320 available bytes; 98.73% used; 110410509 free inodes.

server2 `/var/tmp`: 22852280320 available bytes; 98.73% used; 110410509 free inodes.

server2 `/mnt/raid5`: 334759706624 available bytes; 97.69% used; 445096114 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84438638592 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84438638592 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142392250368 available bytes; 98.03% used; 225812507 free inodes.

server3 `/tmp`: 84438638592 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84438638592 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637466112 available bytes; 94.11% used; 114350349 free inodes.

server4 `/home`: 105637466112 available bytes; 94.11% used; 114350349 free inodes.

server4 `/data`: 249061646336 available bytes; 96.56% used; 225012485 free inodes.

server4 `/tmp`: 105637466112 available bytes; 94.11% used; 114350349 free inodes.

server4 `/var/tmp`: 105637466112 available bytes; 94.11% used; 114350349 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
