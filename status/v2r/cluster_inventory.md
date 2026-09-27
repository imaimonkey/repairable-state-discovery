# V2R cluster inventory

2026-09-27T02:41:38.970028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315079200768 available bytes; 82.42% used; 112443411 free inodes.

server1 `/home`: 315079200768 available bytes; 82.42% used; 112443411 free inodes.

server1 `/tmp`: 315079200768 available bytes; 82.42% used; 112443411 free inodes.

server1 `/var/tmp`: 315079200768 available bytes; 82.42% used; 112443411 free inodes.

server1 `/mnt/raid5`: 637203537920 available bytes; 97.08% used; 337401566 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17625862144 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17625862144 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17625862144 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17625862144 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580631248896 available bytes; 95.99% used; 444884281 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78706876416 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78706876416 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336618889216 available bytes; 81.53% used; 225762185 free inodes.

server3 `/tmp`: 78706876416 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78706876416 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036051456 available bytes; 93.80% used; 114373249 free inodes.

server4 `/home`: 111036051456 available bytes; 93.80% used; 114373249 free inodes.

server4 `/data`: 397019070464 available bytes; 94.51% used; 224781465 free inodes.

server4 `/tmp`: 111036051456 available bytes; 93.80% used; 114373249 free inodes.

server4 `/var/tmp`: 111036051456 available bytes; 93.80% used; 114373249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
