# V2R cluster inventory

2026-09-25T09:47:57.977097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318836682752 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318836682752 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318836682752 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318836682752 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350356041728 available bytes; 98.39% used; 337556813 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22836002816 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22836002816 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22836002816 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22836002816 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331205025792 available bytes; 97.71% used; 445091823 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417093632 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84417093632 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142299439104 available bytes; 98.03% used; 225810357 free inodes.

server3 `/tmp`: 84417093632 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84417093632 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614757888 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614757888 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240047108096 available bytes; 96.68% used; 224993260 free inodes.

server4 `/tmp`: 105614757888 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614757888 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
