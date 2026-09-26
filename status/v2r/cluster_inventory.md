# V2R cluster inventory

2026-09-26T11:24:33.908851+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318208299008 available bytes; 82.25% used; 112474811 free inodes.

server1 `/home`: 318208299008 available bytes; 82.25% used; 112474811 free inodes.

server1 `/tmp`: 318208299008 available bytes; 82.25% used; 112474811 free inodes.

server1 `/var/tmp`: 318208299008 available bytes; 82.25% used; 112474811 free inodes.

server1 `/mnt/raid5`: 218709753856 available bytes; 99.00% used; 337538108 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19785371648 available bytes; 98.90% used; 110383614 free inodes.

server2 `/home`: 19785371648 available bytes; 98.90% used; 110383614 free inodes.

server2 `/tmp`: 19785371648 available bytes; 98.90% used; 110383614 free inodes.

server2 `/var/tmp`: 19785371648 available bytes; 98.90% used; 110383614 free inodes.

server2 `/mnt/raid5`: 241587363840 available bytes; 98.33% used; 444978081 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649120768 available bytes; 95.39% used; 114110821 free inodes.

server3 `/home`: 82649120768 available bytes; 95.39% used; 114110821 free inodes.

server3 `/data`: 123500810240 available bytes; 98.29% used; 225825608 free inodes.

server3 `/tmp`: 82649120768 available bytes; 95.39% used; 114110821 free inodes.

server3 `/var/tmp`: 82649120768 available bytes; 95.39% used; 114110821 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105909743616 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105909743616 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88787206144 available bytes; 98.77% used; 224880326 free inodes.

server4 `/tmp`: 105909743616 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105909743616 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
