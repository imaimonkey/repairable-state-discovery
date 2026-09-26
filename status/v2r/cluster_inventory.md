# V2R cluster inventory

2026-09-26T20:11:45.525996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315540660224 available bytes; 82.40% used; 112445143 free inodes.

server1 `/home`: 315540660224 available bytes; 82.40% used; 112445143 free inodes.

server1 `/tmp`: 315540660224 available bytes; 82.40% used; 112445143 free inodes.

server1 `/var/tmp`: 315540660224 available bytes; 82.40% used; 112445143 free inodes.

server1 `/mnt/raid5`: 645854502912 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18021765120 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18021765120 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18021765120 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18021765120 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 601201684480 available bytes; 95.85% used; 444965035 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81263247360 available bytes; 95.47% used; 114065295 free inodes.

server3 `/home`: 81263247360 available bytes; 95.47% used; 114065295 free inodes.

server3 `/data`: 1348720828416 available bytes; 81.36% used; 225832869 free inodes.

server3 `/tmp`: 81263247360 available bytes; 95.47% used; 114065295 free inodes.

server3 `/var/tmp`: 81263247360 available bytes; 95.47% used; 114065295 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919537152 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919537152 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410264506368 available bytes; 94.33% used; 224824171 free inodes.

server4 `/tmp`: 105919537152 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919537152 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
