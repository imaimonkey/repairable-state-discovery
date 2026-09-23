# V2R cluster inventory

2026-09-23T16:53:45.565965+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41399193600 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41399193600 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41399193600 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41399193600 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 547858923520 available bytes; 96.21% used; 445217323 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 296824369152 available bytes; 83.44% used; 114285485 free inodes.

server3 `/home`: 296824369152 available bytes; 83.44% used; 114285485 free inodes.

server3 `/data`: 95323893760 available bytes; 98.68% used; 225853204 free inodes.

server3 `/tmp`: 296824369152 available bytes; 83.44% used; 114285485 free inodes.

server3 `/var/tmp`: 296824369152 available bytes; 83.44% used; 114285485 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489777664 available bytes; 93.78% used; 114375793 free inodes.

server4 `/home`: 111489777664 available bytes; 93.78% used; 114375793 free inodes.

server4 `/data`: 34119921664 available bytes; 99.53% used; 225477846 free inodes.

server4 `/tmp`: 111489777664 available bytes; 93.78% used; 114375793 free inodes.

server4 `/var/tmp`: 111489777664 available bytes; 93.78% used; 114375793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
