# V2R cluster inventory

2026-09-24T22:16:01.575313+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323948879872 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323948879872 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323948879872 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323948879872 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415402074112 available bytes; 98.09% used; 337621980 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 30113345536 available bytes; 98.32% used; 110411304 free inodes.

server2 `/home`: 30113345536 available bytes; 98.32% used; 110411304 free inodes.

server2 `/tmp`: 30113345536 available bytes; 98.32% used; 110411304 free inodes.

server2 `/var/tmp`: 30113345536 available bytes; 98.32% used; 110411304 free inodes.

server2 `/mnt/raid5`: 488970526720 available bytes; 96.62% used; 445153583 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84381917184 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84381917184 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149514739712 available bytes; 97.93% used; 225802361 free inodes.

server3 `/tmp`: 84381917184 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84381917184 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105810755584 available bytes; 94.10% used; 114348328 free inodes.

server4 `/home`: 105810755584 available bytes; 94.10% used; 114348328 free inodes.

server4 `/data`: 73408360448 available bytes; 98.99% used; 225233349 free inodes.

server4 `/tmp`: 105810755584 available bytes; 94.10% used; 114348328 free inodes.

server4 `/var/tmp`: 105810755584 available bytes; 94.10% used; 114348328 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
