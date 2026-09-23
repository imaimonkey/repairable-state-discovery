# V2R cluster inventory

2026-09-23T15:54:07.215715+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41418190848 available bytes; 97.69% used; 110435191 free inodes.

server2 `/home`: 41418190848 available bytes; 97.69% used; 110435191 free inodes.

server2 `/tmp`: 41418190848 available bytes; 97.69% used; 110435191 free inodes.

server2 `/var/tmp`: 41418190848 available bytes; 97.69% used; 110435191 free inodes.

server2 `/mnt/raid5`: 550223319040 available bytes; 96.20% used; 445223055 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 377015545856 available bytes; 78.96% used; 114293698 free inodes.

server3 `/home`: 377015545856 available bytes; 78.96% used; 114293698 free inodes.

server3 `/data`: 125335371776 available bytes; 98.27% used; 225854723 free inodes.

server3 `/tmp`: 377015545856 available bytes; 78.96% used; 114293698 free inodes.

server3 `/var/tmp`: 377015545856 available bytes; 78.96% used; 114293698 free inodes.
| server4 | True | ['2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499243520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111499243520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 37569396736 available bytes; 99.48% used; 225486673 free inodes.

server4 `/tmp`: 111499243520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111499243520 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
