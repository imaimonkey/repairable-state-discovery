# V2R cluster inventory

2026-09-27T15:09:58.428494+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748171264 available bytes; 83.00% used; 112401393 free inodes.

server1 `/home`: 304748171264 available bytes; 83.00% used; 112401393 free inodes.

server1 `/tmp`: 304748171264 available bytes; 83.00% used; 112401393 free inodes.

server1 `/var/tmp`: 304748171264 available bytes; 83.00% used; 112401393 free inodes.

server1 `/mnt/raid5`: 630112989184 available bytes; 97.11% used; 337424042 free inodes.
| server2 | True | ['0', '2', '3', '4', '5', '6', '7'] | [] | reference_compatible=False |

server2 `/`: 13404872704 available bytes; 99.25% used; 110351806 free inodes.

server2 `/home`: 13404872704 available bytes; 99.25% used; 110351806 free inodes.

server2 `/tmp`: 13404872704 available bytes; 99.25% used; 110351806 free inodes.

server2 `/var/tmp`: 13404872704 available bytes; 99.25% used; 110351806 free inodes.

server2 `/mnt/raid5`: 524488544256 available bytes; 96.38% used; 444721472 free inodes.
| server3 | True | ['0', '1', '2'] | [] | reference_compatible=True |

server3 `/`: 78557528064 available bytes; 95.62% used; 114062765 free inodes.

server3 `/home`: 78557528064 available bytes; 95.62% used; 114062765 free inodes.

server3 `/data`: 1326750134272 available bytes; 81.66% used; 225756317 free inodes.

server3 `/tmp`: 78557528064 available bytes; 95.62% used; 114062765 free inodes.

server3 `/var/tmp`: 78557528064 available bytes; 95.62% used; 114062765 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 108541403136 available bytes; 93.94% used; 114372730 free inodes.

server4 `/home`: 108541403136 available bytes; 93.94% used; 114372730 free inodes.

server4 `/data`: 350405234688 available bytes; 95.16% used; 224727189 free inodes.

server4 `/tmp`: 108541403136 available bytes; 93.94% used; 114372730 free inodes.

server4 `/var/tmp`: 108541403136 available bytes; 93.94% used; 114372730 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
