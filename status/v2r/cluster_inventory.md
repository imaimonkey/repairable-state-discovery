# V2R cluster inventory

2026-09-24T20:37:19.229804+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323981484032 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323981484032 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323981484032 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323981484032 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415613894656 available bytes; 98.09% used; 337633611 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30150770688 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30150770688 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30150770688 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30150770688 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491516125184 available bytes; 96.60% used; 445156961 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84396855296 available bytes; 95.29% used; 114156104 free inodes.

server3 `/home`: 84396855296 available bytes; 95.29% used; 114156104 free inodes.

server3 `/data`: 151349633024 available bytes; 97.91% used; 225804230 free inodes.

server3 `/tmp`: 84396855296 available bytes; 95.29% used; 114156104 free inodes.

server3 `/var/tmp`: 84396855296 available bytes; 95.29% used; 114156104 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639976960 available bytes; 94.10% used; 114348380 free inodes.

server4 `/home`: 105639976960 available bytes; 94.10% used; 114348380 free inodes.

server4 `/data`: 85459218432 available bytes; 98.82% used; 225257609 free inodes.

server4 `/tmp`: 105639976960 available bytes; 94.10% used; 114348380 free inodes.

server4 `/var/tmp`: 105639976960 available bytes; 94.10% used; 114348380 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
