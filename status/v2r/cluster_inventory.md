# V2R cluster inventory

2026-09-25T10:33:53.092113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319000219648 available bytes; 82.20% used; 112479386 free inodes.

server1 `/home`: 319000219648 available bytes; 82.20% used; 112479386 free inodes.

server1 `/tmp`: 319000219648 available bytes; 82.20% used; 112479386 free inodes.

server1 `/var/tmp`: 319000219648 available bytes; 82.20% used; 112479386 free inodes.

server1 `/mnt/raid5`: 364836700160 available bytes; 98.33% used; 337555264 free inodes.
| server2 | True | ['0', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22825005056 available bytes; 98.73% used; 110410496 free inodes.

server2 `/home`: 22825005056 available bytes; 98.73% used; 110410496 free inodes.

server2 `/tmp`: 22825005056 available bytes; 98.73% used; 110410496 free inodes.

server2 `/var/tmp`: 22825005056 available bytes; 98.73% used; 110410496 free inodes.

server2 `/mnt/raid5`: 316112498688 available bytes; 97.82% used; 445089982 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84416761856 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84416761856 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142007005184 available bytes; 98.04% used; 225815671 free inodes.

server3 `/tmp`: 84416761856 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84416761856 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613262848 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613262848 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238521356288 available bytes; 96.70% used; 224986733 free inodes.

server4 `/tmp`: 105613262848 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613262848 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
