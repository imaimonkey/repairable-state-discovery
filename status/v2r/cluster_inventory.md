# V2R cluster inventory

2026-09-27T02:11:11.034935+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315159515136 available bytes; 82.42% used; 112443330 free inodes.

server1 `/home`: 315159515136 available bytes; 82.42% used; 112443330 free inodes.

server1 `/tmp`: 315159515136 available bytes; 82.42% used; 112443330 free inodes.

server1 `/var/tmp`: 315159515136 available bytes; 82.42% used; 112443330 free inodes.

server1 `/mnt/raid5`: 637262974976 available bytes; 97.08% used; 337401674 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17627951104 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17627951104 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17627951104 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17627951104 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 581511196672 available bytes; 95.98% used; 444885190 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78715240448 available bytes; 95.61% used; 114062957 free inodes.

server3 `/home`: 78715240448 available bytes; 95.61% used; 114062957 free inodes.

server3 `/data`: 1338770460672 available bytes; 81.50% used; 225762601 free inodes.

server3 `/tmp`: 78715240448 available bytes; 95.61% used; 114062957 free inodes.

server3 `/var/tmp`: 78715240448 available bytes; 95.61% used; 114062957 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105810440192 available bytes; 94.10% used; 114347750 free inodes.

server4 `/home`: 105810440192 available bytes; 94.10% used; 114347750 free inodes.

server4 `/data`: 403618136064 available bytes; 94.42% used; 224781872 free inodes.

server4 `/tmp`: 105810440192 available bytes; 94.10% used; 114347750 free inodes.

server4 `/var/tmp`: 105810440192 available bytes; 94.10% used; 114347750 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
