# V2R cluster inventory

2026-09-24T08:48:46.493855+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324385595392 available bytes; 81.90% used; 112490272 free inodes.

server1 `/home`: 324385595392 available bytes; 81.90% used; 112490272 free inodes.

server1 `/tmp`: 324385595392 available bytes; 81.90% used; 112490272 free inodes.

server1 `/var/tmp`: 324385595392 available bytes; 81.90% used; 112490272 free inodes.

server1 `/mnt/raid5`: 504242724864 available bytes; 97.69% used; 337718301 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57797705728 available bytes; 96.78% used; 110430946 free inodes.

server2 `/home`: 57797705728 available bytes; 96.78% used; 110430946 free inodes.

server2 `/tmp`: 57797705728 available bytes; 96.78% used; 110430946 free inodes.

server2 `/var/tmp`: 57797705728 available bytes; 96.78% used; 110430946 free inodes.

server2 `/mnt/raid5`: 515578068992 available bytes; 96.44% used; 445179093 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85899087872 available bytes; 95.21% used; 114199578 free inodes.

server3 `/home`: 85899087872 available bytes; 95.21% used; 114199578 free inodes.

server3 `/data`: 173615230976 available bytes; 97.60% used; 225822124 free inodes.

server3 `/tmp`: 85899087872 available bytes; 95.21% used; 114199578 free inodes.

server3 `/var/tmp`: 85899087872 available bytes; 95.21% used; 114199578 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759895552 available bytes; 94.10% used; 114349091 free inodes.

server4 `/home`: 105759895552 available bytes; 94.10% used; 114349091 free inodes.

server4 `/data`: 254538600448 available bytes; 96.48% used; 225273429 free inodes.

server4 `/tmp`: 105759895552 available bytes; 94.10% used; 114349091 free inodes.

server4 `/var/tmp`: 105759895552 available bytes; 94.10% used; 114349091 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
