# V2R cluster inventory

2026-09-27T14:28:44.393811+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304735879168 available bytes; 83.00% used; 112401361 free inodes.

server1 `/home`: 304735879168 available bytes; 83.00% used; 112401361 free inodes.

server1 `/tmp`: 304735879168 available bytes; 83.00% used; 112401361 free inodes.

server1 `/var/tmp`: 304735879168 available bytes; 83.00% used; 112401361 free inodes.

server1 `/mnt/raid5`: 630250778624 available bytes; 97.11% used; 337424058 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13412917248 available bytes; 99.25% used; 110351785 free inodes.

server2 `/home`: 13412917248 available bytes; 99.25% used; 110351785 free inodes.

server2 `/tmp`: 13412917248 available bytes; 99.25% used; 110351785 free inodes.

server2 `/var/tmp`: 13412917248 available bytes; 99.25% used; 110351785 free inodes.

server2 `/mnt/raid5`: 526845923328 available bytes; 96.36% used; 444722154 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78558310400 available bytes; 95.62% used; 114062775 free inodes.

server3 `/home`: 78558310400 available bytes; 95.62% used; 114062775 free inodes.

server3 `/data`: 1328706879488 available bytes; 81.64% used; 225756842 free inodes.

server3 `/tmp`: 78558310400 available bytes; 95.62% used; 114062775 free inodes.

server3 `/var/tmp`: 78558310400 available bytes; 95.62% used; 114062775 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110184542208 available bytes; 93.85% used; 114372779 free inodes.

server4 `/home`: 110184542208 available bytes; 93.85% used; 114372779 free inodes.

server4 `/data`: 350541545472 available bytes; 95.16% used; 224727379 free inodes.

server4 `/tmp`: 110184542208 available bytes; 93.85% used; 114372779 free inodes.

server4 `/var/tmp`: 110184542208 available bytes; 93.85% used; 114372779 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
