# V2R cluster inventory

2026-09-25T10:07:15.758419+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318834704384 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318834704384 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318834704384 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318834704384 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 365946081280 available bytes; 98.32% used; 337556917 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22827016192 available bytes; 98.73% used; 110410470 free inodes.

server2 `/home`: 22827016192 available bytes; 98.73% used; 110410470 free inodes.

server2 `/tmp`: 22827016192 available bytes; 98.73% used; 110410470 free inodes.

server2 `/var/tmp`: 22827016192 available bytes; 98.73% used; 110410470 free inodes.

server2 `/mnt/raid5`: 316844937216 available bytes; 97.81% used; 445091341 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418301952 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418301952 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 141958717440 available bytes; 98.04% used; 225809467 free inodes.

server3 `/tmp`: 84418301952 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418301952 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614184448 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614184448 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240008949760 available bytes; 96.68% used; 224990824 free inodes.

server4 `/tmp`: 105614184448 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614184448 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
