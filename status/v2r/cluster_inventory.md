# V2R cluster inventory

2026-09-23T19:03:29.651703+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325946994688 available bytes; 81.82% used; 112510914 free inodes.

server1 `/home`: 325946994688 available bytes; 81.82% used; 112510914 free inodes.

server1 `/tmp`: 325946994688 available bytes; 81.82% used; 112510914 free inodes.

server1 `/var/tmp`: 325946994688 available bytes; 81.82% used; 112510914 free inodes.

server1 `/mnt/raid5`: 1389249404928 available bytes; 93.63% used; 337741434 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41339056128 available bytes; 97.69% used; 110435438 free inodes.

server2 `/home`: 41339056128 available bytes; 97.69% used; 110435438 free inodes.

server2 `/tmp`: 41339056128 available bytes; 97.69% used; 110435438 free inodes.

server2 `/var/tmp`: 41339056128 available bytes; 97.69% used; 110435438 free inodes.

server2 `/mnt/raid5`: 543945900032 available bytes; 96.24% used; 445213449 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293385728000 available bytes; 83.63% used; 114225553 free inodes.

server3 `/home`: 293385728000 available bytes; 83.63% used; 114225553 free inodes.

server3 `/data`: 52774981632 available bytes; 99.27% used; 225846006 free inodes.

server3 `/tmp`: 293385728000 available bytes; 83.63% used; 114225553 free inodes.

server3 `/var/tmp`: 293385728000 available bytes; 83.63% used; 114225553 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106475450368 available bytes; 94.06% used; 114356232 free inodes.

server4 `/home`: 106475450368 available bytes; 94.06% used; 114356232 free inodes.

server4 `/data`: 12632064 available bytes; 100.00% used; 225457663 free inodes.

server4 `/tmp`: 106475450368 available bytes; 94.06% used; 114356232 free inodes.

server4 `/var/tmp`: 106475450368 available bytes; 94.06% used; 114356232 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
