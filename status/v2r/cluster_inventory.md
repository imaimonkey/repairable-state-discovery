# V2R cluster inventory

2026-09-26T09:02:39.473438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318737481728 available bytes; 82.22% used; 112475808 free inodes.

server1 `/home`: 318737481728 available bytes; 82.22% used; 112475808 free inodes.

server1 `/tmp`: 318737481728 available bytes; 82.22% used; 112475808 free inodes.

server1 `/var/tmp`: 318737481728 available bytes; 82.22% used; 112475808 free inodes.

server1 `/mnt/raid5`: 219023273984 available bytes; 99.00% used; 337538778 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316130304 available bytes; 98.76% used; 110403913 free inodes.

server2 `/home`: 22316130304 available bytes; 98.76% used; 110403913 free inodes.

server2 `/tmp`: 22316130304 available bytes; 98.76% used; 110403913 free inodes.

server2 `/var/tmp`: 22316130304 available bytes; 98.76% used; 110403913 free inodes.

server2 `/mnt/raid5`: 255005614080 available bytes; 98.24% used; 445023935 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82660876288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/home`: 82660876288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/data`: 123661230080 available bytes; 98.29% used; 225828242 free inodes.

server3 `/tmp`: 82660876288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/var/tmp`: 82660876288 available bytes; 95.39% used; 114110812 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106046369792 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106046369792 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89343635456 available bytes; 98.77% used; 224883338 free inodes.

server4 `/tmp`: 106046369792 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106046369792 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
